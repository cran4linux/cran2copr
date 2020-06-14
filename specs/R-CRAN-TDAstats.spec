%global packname  TDAstats
%global packver   0.4.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.1
Release:          2%{?dist}
Summary:          Pipeline for Topological Data Analysis

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3
Requires:         R-core >= 3.3
BuildRequires:    R-CRAN-ggplot2 >= 2.2.1
BuildRequires:    R-CRAN-Rcpp >= 0.12.15
Requires:         R-CRAN-ggplot2 >= 2.2.1
Requires:         R-CRAN-Rcpp >= 0.12.15

%description
A comprehensive toolset for any useR conducting topological data analysis,
specifically via the calculation of persistent homology in a Vietoris-Rips
complex. The tools this package currently provides can be conveniently
split into three main sections: (1) calculating persistent homology; (2)
conducting statistical inference on persistent homology calculations; (3)
visualizing persistent homology and statistical inference. The published
form of TDAstats can be found in Wadhwa et al. (2018)
<doi:10.21105/joss.00860>. For a general background on computing
persistent homology for topological data analysis, see Otter et al. (2017)
<doi:10.1140/epjds/s13688-017-0109-5>. To learn more about how the
permutation test is used for nonparametric statistical inference in
topological data analysis, read Robinson & Turner (2017)
<doi:10.1007/s41468-017-0008-7>. To learn more about how TDAstats
calculates persistent homology, you can visit the GitHub repository for
Ripser, the software that works behind the scenes at
<https://github.com/Ripser/ripser>. This package has been published as
Wadhwa et al. (2018) <doi:10.21105/joss.00860>.

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
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
