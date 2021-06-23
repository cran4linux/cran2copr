%global __brp_check_rpaths %{nil}
%global packname  AmericanCallOpt
%global packver   0.95
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.95
Release:          3%{?dist}%{?buildtag}
Summary:          This package includes pricing function for selected Americancall options with underlying assets that generate payouts.

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.0.0
Requires:         R-core >= 2.0.0
BuildArch:        noarch

%description
This package includes a set of pricing functions for American call
options. The following cases are covered: Pricing of an American call
using the standard binomial approximation; Hedge parameters for an
American call with a standard binomial tree; Binomial pricing of an
American call with continuous payout from the underlying asset; Binomial
pricing of an American call with an underlying stock that pays
proportional dividends in discrete time; Pricing of an American call on
futures using a binomial approximation; Pricing of a currency futures
American call using a binomial approximation; Pricing of a perpetual
American call. The user should kindly notice that this material is for
educational purposes only. The codes are not optimized for computational
efficiency as they are meant to represent standard cases of analytical and
numerical solution.

%prep
%setup -q -c -n %{packname}


%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/help
%doc %{rlibdir}/%{packname}/demo
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
