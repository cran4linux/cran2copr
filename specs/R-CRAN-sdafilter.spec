%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  sdafilter
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Symmetrized Data Aggregation

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-CRAN-glasso 
BuildRequires:    R-CRAN-POET 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-selectiveInference 
Requires:         R-CRAN-glmnet 
Requires:         R-CRAN-glasso 
Requires:         R-CRAN-POET 
Requires:         R-stats 
Requires:         R-CRAN-selectiveInference 

%description
We develop a new class of distribution free multiple testing rules for
false discovery rate (FDR) control under general dependence. A key element
in our proposal is a symmetrized data aggregation (SDA) approach to
incorporating the dependence structure via sample splitting, data
screening and information pooling. The proposed SDA filter first
constructs a sequence of ranking statistics that fulfill global symmetry
properties, and then chooses a data driven threshold along the ranking to
control the FDR. For more information, see the website below and the
accompanying paper: Du et al. (2023), "False Discovery Rate Control Under
General Dependence By Symmetrized Data Aggregation",
<doi:10.1080/01621459.2021.1945459>. Some optional functionality uses the
archived R packages ‘huge’ and ‘pfa’, which are not available from CRAN’s
main repositories. Users who need this optional functionality can obtain
them from the CRAN Archive as follows: ‘huge’ at
<https://cran.r-project.org/src/contrib/Archive/huge/>; ‘pfa’ at
<https://cran.r-project.org/src/contrib/Archive/pfa/>.

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
