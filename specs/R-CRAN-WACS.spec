%global packname  WACS
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          1%{?dist}
Summary:          Multivariate Weather-State Approach Conditionally Skew-NormalGenerator

License:          GPL (>= 2.0)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-mclust 
BuildRequires:    R-CRAN-mnormt 
BuildRequires:    R-CRAN-tmvtnorm 
BuildRequires:    R-CRAN-mvtnorm 
Requires:         R-CRAN-mclust 
Requires:         R-CRAN-mnormt 
Requires:         R-CRAN-tmvtnorm 
Requires:         R-CRAN-mvtnorm 

%description
A multivariate weather generator for daily climate variables based on
weather-states (Flecher et al. (2010) <doi:10.1029/2009WR008098>). It uses
a Markov chain for modeling the succession of weather states.
Conditionally to the weather states, the multivariate variables are
modeled using the family of Complete Skew-Normal distributions. Parameters
are estimated on measured series. Must include the variable 'Rain' and can
accept as many other variables as desired.

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

%files
%{rlibdir}/%{packname}
