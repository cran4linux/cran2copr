%global packname  GeneNet
%global packver   1.2.15
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.15
Release:          3%{?dist}%{?buildtag}
Summary:          Modeling and Inferring Gene Networks

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.2
Requires:         R-core >= 3.0.2
BuildArch:        noarch
BuildRequires:    R-CRAN-corpcor >= 1.6.9
BuildRequires:    R-CRAN-fdrtool >= 1.2.15
BuildRequires:    R-CRAN-longitudinal >= 1.1.12
BuildRequires:    R-stats 
BuildRequires:    R-grDevices 
Requires:         R-CRAN-corpcor >= 1.6.9
Requires:         R-CRAN-fdrtool >= 1.2.15
Requires:         R-CRAN-longitudinal >= 1.1.12
Requires:         R-stats 
Requires:         R-grDevices 

%description
Analyzes gene expression (time series) data with focus on the inference of
gene networks. In particular, GeneNet implements the methods of Schaefer
and Strimmer (2005a,b,c) and Opgen-Rhein and Strimmer (2006, 2007) for
learning large-scale gene association networks (including assignment of
putative directions).

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
