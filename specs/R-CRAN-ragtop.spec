%global __brp_check_rpaths %{nil}
%global packname  ragtop
%global packver   1.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.1
Release:          3%{?dist}%{?buildtag}
Summary:          Pricing Equity Derivatives with Extensions of Black-Scholes

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-methods >= 3.2.2
BuildRequires:    R-CRAN-limSolve >= 1.5.5.1
BuildRequires:    R-CRAN-futile.logger >= 1.4.1
Requires:         R-methods >= 3.2.2
Requires:         R-CRAN-limSolve >= 1.5.5.1
Requires:         R-CRAN-futile.logger >= 1.4.1

%description
Algorithms to price American and European equity options, convertible
bonds and a variety of other financial derivatives. It uses an extension
of the usual Black-Scholes model in which jump to default may occur at a
probability specified by a power-law link between stock price and hazard
rate as found in the paper by Takahashi, Kobayashi, and Nakagawa (2001)
<doi:10.3905/jfi.2001.319302>.  We use ideas and techniques from Andersen
and Buffum (2002) <doi:10.2139/ssrn.355308> and Linetsky (2006)
<doi:10.1111/j.1467-9965.2006.00271.x>.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;

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
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
