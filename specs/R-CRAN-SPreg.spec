%global __brp_check_rpaths %{nil}
%global packname  SPreg
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          2%{?dist}%{?buildtag}
Summary:          Bias Reduction in the Skew-Probit Model for a Binary Response

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0
Requires:         R-core >= 3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-sn 
BuildRequires:    R-CRAN-ucminf 
Requires:         R-CRAN-sn 
Requires:         R-CRAN-ucminf 

%description
Provides a function for the estimation of parameters in a binary
regression with the skew-probit link function. Naive MLE, Jeffrey type of
prior and Cauchy prior type of penalization are implemented, as described
in DongHyuk Lee and Samiran Sinha (2019+)
<doi:10.1080/00949655.2019.1590579>.

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
