%global __brp_check_rpaths %{nil}
%global packname  SpatialPack
%global packver   0.3-8196
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.8196
Release:          1%{?dist}%{?buildtag}
Summary:          Tools for Assessment the Association Between Two Spatial Processes

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-fastmatrix 
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
Requires:         R-CRAN-fastmatrix 
Requires:         R-stats 
Requires:         R-graphics 

%description
Tools to assess the association between two spatial processes. Currently,
several methodologies are implemented: A modified t-test to perform
hypothesis testing about the independence between the processes, a
suitable nonparametric correlation coefficient, the codispersion
coefficient, and an F test for assessing the multiple correlation between
one spatial process and several others. Functions for image processing and
computing the spatial association between images are also provided.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
