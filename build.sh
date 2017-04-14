#!/bin/bash
set -e

# Note: must manually update Version in RPM_SPECFILE: vertx.spec

# RPMBUILD_DIR=`rpm --eval %{_topdir}`
RPMBUILD_DIR=tmp_$(date +%s)
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
echo "=================================================================="
echo "rpmbuild \
         --BUILDROOT=$VERTX_RPM_DIR/$RPMBUILD_DIR --clean -ba $RPMBUILD_DIR/SPECS/vertx.spec"
rpmbuild --BUILDROOT=$VERTX_RPM_DIR/$RPMBUILD_DIR --clean -ba $RPMBUILD_DIR/SPECS/vertx.spec
