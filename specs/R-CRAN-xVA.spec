%global __brp_check_rpaths %{nil}
%global packname  xVA
%global packver   0.8.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.8.5
Release:          1%{?dist}%{?buildtag}
Summary:          Calculates Credit Risk Valuation Adjustments

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-SACCR 
BuildRequires:    R-CRAN-Trading 
Requires:         R-methods 
Requires:         R-CRAN-SACCR 
Requires:         R-CRAN-Trading 

%description
Calculates a number of valuation adjustments including CVA, DVA, FBA, FCA,
MVA and KVA. A two-way margin agreement has been implemented. For the KVA
calculation three regulatory frameworks are supported: CEM, (simplified)
SA-CCR, OEM and IMM. The probability of default is implied through the
credit spreads curve. Currently, only IRSwaps are supported. For more
information, you can check one of the books regarding xVA:
<http://www.cvacentral.com/books/credit-value-adjustment>.

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
