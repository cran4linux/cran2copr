%global packname  revengc
%global packver   1.0.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.4
Release:          3%{?dist}%{?buildtag}
Summary:          Reverse Engineering Summarized Data

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-mipfp 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-truncdist 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-mipfp 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-truncdist 

%description
Decoupled (e.g. separate averages) and censored (e.g. > 100 species)
variables are continually reported by many well-established organizations
(e.g. World Health Organization (WHO), Centers for Disease Control and
Prevention (CDC), World Bank, and various national censuses).  The
challenge therefore is to infer what the original data could have been
given summarized information.  We present an R package that reverse
engineers decoupled and/or censored count data with two main functions.
The cnbinom.pars function estimates the average and dispersion parameter
of a censored univariate frequency table.  The rec function reverse
engineers summarized data into an uncensored bivariate table of
probabilities.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
