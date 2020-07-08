%global packname  DetLifeInsurance
%global packver   0.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.2
Release:          1%{?dist}
Summary:          Life Insurance Premium and Reserves Valuation

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch

%description
Methods for valuation of life insurance premiums and reserves (including
variable-benefit and fractional coverage) based on "Actuarial Mathematics"
by Bowers, H.U. Gerber, J.C. Hickman, D.A. Jones and C.J. Nesbitt (1997,
ISBN: 978-0938959465), "Actuarial Mathematics for Life Contingent Risks"
by Dickson, David C. M., Hardy, Mary R. and Waters, Howard R (2009)
<doi:10.1017/CBO9780511800146> and "Life Contingencies" by Jordan, C. W
(1952) <doi:10.1017/S002026810005410X>. It also contains functions for
equivalent interest and discount rate calculation, present and future
values of annuities, and loan amortization schedule.

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
