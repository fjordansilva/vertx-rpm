#!/bin/bash
set -e

# Note: Manually update Version in the vertx.spec RPM spec file.
#       The RPM build process downloads that version from Source.

RPMBUILD_DIR=`rpm --eval %{_topdir}`
mkdir -p $RPMBUILD_DIR/{BUILD,RPMS,SOURCES,SPECS,SRPMS}

echo  $RPMBUILD_DIR
echo  `dirname $0` 
pushd `dirname $0` > /dev/null
VERTX_RPM_DIR=$(pwd)
popd > /dev/null

cd $RPMBUILD_DIR/SPECS
cp $VERTX_RPM_DIR/*.spec .
cd -

spectool -g -R $RPMBUILD_DIR/SPECS/vertx.spec
echo "rpmbuild --clean -ba $RPMBUILD_DIR/SPECS/vertx.spec"
rpmbuild       --clean -ba $RPMBUILD_DIR/SPECS/vertx.spec
