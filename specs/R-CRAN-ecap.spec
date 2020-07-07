%global packname  ecap
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          2%{?dist}
Summary:          Excess Certainty Adjusted Probability Estimate

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-splines >= 3.6.0
BuildRequires:    R-CRAN-quadprog >= 1.5.7
BuildRequires:    R-CRAN-ggplot2 
Requires:         R-splines >= 3.6.0
Requires:         R-CRAN-quadprog >= 1.5.7
Requires:         R-CRAN-ggplot2 

%description
Implements the Excess Certainty Adjusted Probability adjustment procedure
as described in the paper "Irrational Exuberance: Correcting Bias in
Probability Estimates" by Gareth James, Peter Radchenko, and Bradley Rava
(Journal of the American Statistical Association, 2020;
<arXiv:1910.13570>). The package includes a function that preforms the
ECAP adjustment and a function that estimates the parameters needed for
implementing ECAP. For testing and reproducibility, the ESPN and
FiveThirtyEight data used in the paper are also included.

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
