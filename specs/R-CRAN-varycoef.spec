%global packname  varycoef
%global packver   0.2.12
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.12
Release:          1%{?dist}
Summary:          Modeling Spatially Varying Coefficients

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-optimParallel >= 0.8.1
BuildRequires:    R-CRAN-spam 
BuildRequires:    R-CRAN-RandomFields 
BuildRequires:    R-CRAN-sp 
Requires:         R-CRAN-optimParallel >= 0.8.1
Requires:         R-CRAN-spam 
Requires:         R-CRAN-RandomFields 
Requires:         R-CRAN-sp 

%description
Implements a maximum likelihood estimation (MLE) method for estimation and
prediction in spatially varying coefficient (SVC) models (Dambon et al.
(2020) <arXiv:2001.08089>). Covariance tapering (Furrer et al. (2006)
<doi:10.1198/106186006X132178>) can be applied such that the method scales
to large data.

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
