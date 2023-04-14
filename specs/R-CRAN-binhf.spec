%global __brp_check_rpaths %{nil}
%global packname  binhf
%global packver   1.0-3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.3
Release:          3%{?dist}%{?buildtag}
Summary:          Haar-Fisz Functions for Binomial Data

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-adlift >= 0.9.2
BuildRequires:    R-CRAN-wavethresh 
BuildRequires:    R-CRAN-EbayesThresh 
Requires:         R-CRAN-adlift >= 0.9.2
Requires:         R-CRAN-wavethresh 
Requires:         R-CRAN-EbayesThresh 

%description
Binomial Haar-Fisz transforms for Gaussianization as in Nunes and Nason
(2009).

%prep
%setup -q -c -n %{packname}


%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%{rlibdir}/%{packname}
