%global packname  gscaLCA
%global packver   0.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.2
Release:          1%{?dist}
Summary:          Generalized Structure Component Analysis- Latent Class Analysis

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-progress 
BuildRequires:    R-CRAN-psych 
BuildRequires:    R-CRAN-fastDummies 
BuildRequires:    R-CRAN-fclust 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-devtools 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-doSNOW 
Requires:         R-CRAN-gridExtra 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-progress 
Requires:         R-CRAN-psych 
Requires:         R-CRAN-fastDummies 
Requires:         R-CRAN-fclust 
Requires:         R-MASS 
Requires:         R-CRAN-devtools 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-doSNOW 

%description
Execute Latent Class Analysis (LCA) by using Generalized Structured
Component Analysis (GSCA). This is explained in Ryoo, Park, and Kim (2009)
<doi:10.1007/s41237-019-00084-6>. It estimates the parameters of latent
class prevalence and item response probability in LCA with a single line
comment. It also provide graphs of item response probabilities.

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
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
