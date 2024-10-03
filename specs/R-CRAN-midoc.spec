%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  midoc
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          A Decision-Making System for Multiple Imputation

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6
Requires:         R-core >= 3.6
BuildArch:        noarch
BuildRequires:    R-CRAN-mice >= 3.16.0
BuildRequires:    R-CRAN-arm 
BuildRequires:    R-CRAN-blorr 
BuildRequires:    R-CRAN-dagitty 
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-lifecycle 
BuildRequires:    R-CRAN-mfp2 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-rmarkdown 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-mice >= 3.16.0
Requires:         R-CRAN-arm 
Requires:         R-CRAN-blorr 
Requires:         R-CRAN-dagitty 
Requires:         R-CRAN-glue 
Requires:         R-grDevices 
Requires:         R-CRAN-lifecycle 
Requires:         R-CRAN-mfp2 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-rmarkdown 
Requires:         R-stats 
Requires:         R-utils 

%description
A guidance system for analysis with missing data. It incorporates expert,
up-to-date methodology to help researchers choose the most appropriate
analysis approach when some data are missing. You provide the available
data and the assumed causal structure, including the likely causes of
missing data. 'midoc' will advise which analysis approaches can be used,
and how best to perform them. 'midoc' follows the framework for the
treatment and reporting of missing data in observational studies (TARMOS).
Lee et al (2021). <doi:10.1016/j.jclinepi.2021.01.008>.

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
