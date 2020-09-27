%global packname  modelbased
%global packver   0.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.0
Release:          1%{?dist}%{?buildtag}
Summary:          Estimation of Model-Based Predictions, Contrasts and Means

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-emmeans >= 1.4.4
BuildRequires:    R-CRAN-insight >= 0.7.1
BuildRequires:    R-CRAN-bayestestR >= 0.4.0
BuildRequires:    R-CRAN-parameters >= 0.3.0
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-emmeans >= 1.4.4
Requires:         R-CRAN-insight >= 0.7.1
Requires:         R-CRAN-bayestestR >= 0.4.0
Requires:         R-CRAN-parameters >= 0.3.0
Requires:         R-graphics 
Requires:         R-stats 
Requires:         R-utils 

%description
Implements a general interface for model-based estimations for a wide
variety of models (see support list of insight; Lüdecke, Waggoner &
Makowski (2019) <doi:10.21105/joss.01412>), used in the computation of
marginal means, contrast analysis and predictions.

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
