%global packname  conogive
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          2%{?dist}%{?buildtag}
Summary:          Congeneric Normal-Ogive Model

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-psych 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-checkmate 
BuildRequires:    R-CRAN-assertthat 
Requires:         R-CRAN-psych 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-checkmate 
Requires:         R-CRAN-assertthat 

%description
The congeneric normal-ogive model is a popular model for psychometric data
(McDonald, R. P. (1997) <doi:10.1007/978-1-4757-2691-6_15>). This model
estimates the model, calculates theoretical and concrete reliability
coefficients, and predicts the latent variable of the model. This is the
companion package to Moss (2020) <doi:10.31234/osf.io/nvg5d>.

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
