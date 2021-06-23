%global __brp_check_rpaths %{nil}
%global packname  ppgmmga
%global packver   1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2
Release:          3%{?dist}%{?buildtag}
Summary:          Projection Pursuit Based on Gaussian Mixtures and EvolutionaryAlgorithms

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4
Requires:         R-core >= 3.4
BuildRequires:    R-CRAN-mclust >= 5.4
BuildRequires:    R-CRAN-ggthemes >= 3.4.0
BuildRequires:    R-CRAN-GA >= 3.1
BuildRequires:    R-CRAN-ggplot2 >= 2.2.1
BuildRequires:    R-CRAN-Rcpp >= 1.0.0
BuildRequires:    R-CRAN-RcppArmadillo >= 0.7
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-crayon 
BuildRequires:    R-utils 
BuildRequires:    R-stats 
Requires:         R-CRAN-mclust >= 5.4
Requires:         R-CRAN-ggthemes >= 3.4.0
Requires:         R-CRAN-GA >= 3.1
Requires:         R-CRAN-ggplot2 >= 2.2.1
Requires:         R-CRAN-Rcpp >= 1.0.0
Requires:         R-CRAN-cli 
Requires:         R-CRAN-crayon 
Requires:         R-utils 
Requires:         R-stats 

%description
Projection Pursuit (PP) algorithm for dimension reduction based on
Gaussian Mixture Models (GMMs) for density estimation using Genetic
Algorithms (GAs) to maximise an approximated negentropy index. For more
details see Scrucca and Serafini (2019)
<doi:10.1080/10618600.2019.1598871>.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/scripts
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
