%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  qapproach
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          The Q Approach to Consensus Building

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-fmsb 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-qmethod 
BuildRequires:    R-CRAN-withr 
Requires:         R-CRAN-fmsb 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-qmethod 
Requires:         R-CRAN-withr 

%description
Implements a workflow based on Q method to support consensus-building
processes. It prepares participant rankings, selects and fits group
perspectives, calculates consensus priority scores, validates results by
bootstrap resampling, and produces publication-ready figures. The
underlying method is described by Geschke et al. (2022) "The Q approach to
consensus building: integrating diverse perspectives to guide
decision-making" <doi:10.32942/X2F59S>.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
[ -d %{packname}/src ] && find %{packname}/src/Make* -type f -exec \
  sed -i 's@-g0@@g' {} \; || true
# don't allow local prefix in executable scripts
find -type f -executable -exec sed -Ei 's@#!( )*/usr/local/bin@#!/usr/bin@g' {} \;

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
# remove buildroot from installed files
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
