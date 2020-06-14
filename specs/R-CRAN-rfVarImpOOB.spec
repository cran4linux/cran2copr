%global packname  rfVarImpOOB
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          2%{?dist}
Summary:          Unbiased Variable Importance for Random Forests

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.2
Requires:         R-core >= 3.2.2
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-randomForest 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-binaryLogic 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-titanic 
BuildRequires:    R-CRAN-prob 
BuildRequires:    R-CRAN-ggpubr 
BuildRequires:    R-CRAN-magrittr 
Requires:         R-stats 
Requires:         R-CRAN-randomForest 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-binaryLogic 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-titanic 
Requires:         R-CRAN-prob 
Requires:         R-CRAN-ggpubr 
Requires:         R-CRAN-magrittr 

%description
Computes a novel variable importance for random forests: Impurity
reduction importance scores for out-of-bag (OOB) data complementing the
existing inbag Gini importance, see also Strobl et al (2007)
<doi:10.1186/1471-2105-8-25>, Strobl et al (2007)
<doi:10.1016/j.csda.2006.12.030> and Breiman (2001)
<DOI:10.1023/A:1010933404324>. The Gini impurities for inbag and OOB data
are combined in three different ways, after which the information gain is
computed at each split. This gain is aggregated for each split variable in
a tree and averaged across trees.

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
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
