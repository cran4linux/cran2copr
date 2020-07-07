%global packname  hier.part
%global packver   1.0-6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.6
Release:          3%{?dist}
Summary:          Hierarchical Partitioning

License:          GPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-gtools 
BuildRequires:    R-CRAN-betareg 
BuildRequires:    R-MASS 
Requires:         R-CRAN-gtools 
Requires:         R-CRAN-betareg 
Requires:         R-MASS 

%description
Partitioning of the independent and joint contributions of each variable
in a multivariate data set, to a linear regression by hierarchical
decomposition of goodness-of-fit measures of regressions using all subsets
of predictors in the data set. (i.e., model (1), (2), ..., (N), (1,2),
..., (1,N), ..., (1,2,3,...,N)). A Z-score based estimate of the
'importance' of each predictor is provided by using a randomisation test.

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
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
