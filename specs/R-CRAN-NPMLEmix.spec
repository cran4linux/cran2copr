%global __brp_check_rpaths %{nil}
%global packname  NPMLEmix
%global packver   1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2
Release:          1%{?dist}%{?buildtag}
Summary:          Two-Groups Mixture Model with Covariates

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.1
Requires:         R-core >= 3.0.1
BuildArch:        noarch
BuildRequires:    R-CRAN-Rmosek 
BuildRequires:    R-CRAN-R.utils 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-spatstat 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-latexpdf 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-FDRreg 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-REBayes 
BuildRequires:    R-CRAN-CAMAN 
BuildRequires:    R-CRAN-progress 
BuildRequires:    R-CRAN-pbapply 
BuildRequires:    R-CRAN-Hmisc 
BuildRequires:    R-CRAN-pracma 
BuildRequires:    R-CRAN-mosaic 
Requires:         R-CRAN-Rmosek 
Requires:         R-CRAN-R.utils 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-spatstat 
Requires:         R-methods 
Requires:         R-CRAN-latexpdf 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-FDRreg 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-REBayes 
Requires:         R-CRAN-CAMAN 
Requires:         R-CRAN-progress 
Requires:         R-CRAN-pbapply 
Requires:         R-CRAN-Hmisc 
Requires:         R-CRAN-pracma 
Requires:         R-CRAN-mosaic 

%description
We develop three procedures for estimation in a two-groups model with
covariates. One of them is a nonparametric maximum likelihood estimation
based approach when the signal distribution is an infinite Gaussian
location mixture and the signal proportion is a logistic function of the
available covariates. Two other functions - marg1() and marg2() have also
been implemented for inference in the above framework. All these methods
can be used for inference in multiple hypotheses testing. For more
information, see the paper: Deb, Saha, Guntuboyina and Sen (2019),
''Two-component Mixture Model in the Presence of Covariates''
<arXiv:1810.07897v2>.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
