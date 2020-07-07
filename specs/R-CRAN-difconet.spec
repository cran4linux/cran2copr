%global packname  difconet
%global packver   1.0-4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.4
Release:          3%{?dist}
Summary:          Differential Coexpressed Networks

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-gplots 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
Requires:         R-CRAN-gplots 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-mvtnorm 
Requires:         R-graphics 
Requires:         R-grDevices 

%description
Estimation of DIFferential COexpressed NETworks using diverse and user
metrics. This package is basically used for three functions related to the
estimation of differential coexpression. First, to estimate differential
coexpression where the coexpression is estimated, by default, by Spearman
correlation. For this, a metric to compare two correlation distributions
is needed. The package includes 6 metrics. Some of them needs a threshold.
A new metric can also be specified as a user function with specific
parameters (see difconet.run). The significance is be estimated by
permutations. Second, to generate datasets with controlled differential
correlation data. This is done by either adding noise, or adding specific
correlation structure. Third, to show the results of differential
correlation analyses. Please see
<http://bioinformatica.mty.itesm.mx/difconet> for further information.

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
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
