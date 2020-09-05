%global packname  tram
%global packver   0.5-1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.1
Release:          1%{?dist}%{?buildtag}
Summary:          Transformation Models

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-mlt >= 1.2.0
BuildRequires:    R-CRAN-basefun >= 1.0.5
BuildRequires:    R-CRAN-variables >= 1.0.2
BuildRequires:    R-CRAN-Formula 
BuildRequires:    R-CRAN-multcomp 
BuildRequires:    R-CRAN-sandwich 
BuildRequires:    R-stats 
BuildRequires:    R-survival 
BuildRequires:    R-graphics 
BuildRequires:    R-Matrix 
BuildRequires:    R-methods 
Requires:         R-CRAN-mlt >= 1.2.0
Requires:         R-CRAN-basefun >= 1.0.5
Requires:         R-CRAN-variables >= 1.0.2
Requires:         R-CRAN-Formula 
Requires:         R-CRAN-multcomp 
Requires:         R-CRAN-sandwich 
Requires:         R-stats 
Requires:         R-survival 
Requires:         R-graphics 
Requires:         R-Matrix 
Requires:         R-methods 

%description
Formula-based user-interfaces to specific transformation models
implemented in package 'mlt'. Available models include Cox models, some
parametric survival models (Weibull, etc.), models for ordered categorical
variables, normal and non-normal (Box-Cox type) linear models, and
continuous outcome logistic regression (Lohse et al., 2017,
<DOI:10.12688/f1000research.12934.1>). The underlying theory is described
in Hothorn et al. (2018) <DOI:10.1111/sjos.12291>. An extension to
transformation models for clustered data is provided (Hothorn, 2019,
<arxiv:1910.09219>). Multivariate conditional transformation models
(<arxiv:1906.03151>) can be fitted as well.

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
