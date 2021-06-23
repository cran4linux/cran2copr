%global __brp_check_rpaths %{nil}
%global packname  CDVineCopulaConditional
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          3%{?dist}%{?buildtag}
Summary:          Sampling from Conditional C- and D-Vine Copulas

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-combinat 
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-VineCopula 
Requires:         R-CRAN-combinat 
Requires:         R-graphics 
Requires:         R-stats 
Requires:         R-CRAN-VineCopula 

%description
Provides tools for sampling from a conditional copula density decomposed
via Pair-Copula Constructions as C- or D- vine. Here, the vines which can
be used for such a sampling are those which sample as first the
conditioning variables (when following the sampling algorithms shown in
Aas et al. (2009) <DOI:10.1016/j.insmatheco.2007.02.001>). The used
sampling algorithm is presented and discussed in Bevacqua et al. (2017)
<DOI:10.5194/hess-2016-652>, and it is a modified version of that from Aas
et al. (2009) <DOI:10.1016/j.insmatheco.2007.02.001>. A function is
available to select the best vine (based on information criteria) among
those which allow for such a conditional sampling. The package includes a
function to compare scatterplot matrices and pair-dependencies of two
multivariate datasets.

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
%{rlibdir}/%{packname}/INDEX
