%global packname  RNAseqNet
%global packver   0.1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.3
Release:          1%{?dist}
Summary:          Log-Linear Poisson Graphical Model with Hot-Deck MultipleImputation

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-igraph >= 1.0
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-hot.deck 
BuildRequires:    R-CRAN-PoiClaClu 
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-methods 
BuildRequires:    R-utils 
Requires:         R-CRAN-igraph >= 1.0
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-hot.deck 
Requires:         R-CRAN-PoiClaClu 
Requires:         R-CRAN-glmnet 
Requires:         R-methods 
Requires:         R-utils 

%description
Infer log-linear Poisson Graphical Model with an auxiliary data set.
Hot-deck multiple imputation method is used to improve the reliability of
the inference with an auxiliary dataset. Standard log-linear Poisson
graphical model can also be used for the inference and the Stability
Approach for Regularization Selection (StARS) is implemented to drive the
selection of the regularization parameter. The method is fully described
in <doi:10.1093/bioinformatics/btx819>.

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
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/misc
%{rlibdir}/%{packname}/INDEX
