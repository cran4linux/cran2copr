%global __brp_check_rpaths %{nil}
%global packname  effects
%global packver   4.2-0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          4.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Effect Displays for Linear, Generalized Linear, and Other Models

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-carData 
BuildRequires:    R-CRAN-lme4 
BuildRequires:    R-nnet 
BuildRequires:    R-lattice 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-colorspace 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-survey 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-estimability 
BuildRequires:    R-CRAN-insight 
Requires:         R-CRAN-carData 
Requires:         R-CRAN-lme4 
Requires:         R-nnet 
Requires:         R-lattice 
Requires:         R-grid 
Requires:         R-CRAN-colorspace 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-stats 
Requires:         R-CRAN-survey 
Requires:         R-utils 
Requires:         R-CRAN-estimability 
Requires:         R-CRAN-insight 

%description
Graphical and tabular effect displays, e.g., of interactions, for various
statistical models with linear predictors.

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
