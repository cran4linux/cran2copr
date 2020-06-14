%global packname  KOBT
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          2%{?dist}
Summary:          Knockoff Boosted Tree

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-glmnet >= 2.0.18
BuildRequires:    R-CRAN-Rdpack >= 0.11.0
BuildRequires:    R-CRAN-knockoff 
BuildRequires:    R-CRAN-spcov 
BuildRequires:    R-CRAN-xgboost 
BuildRequires:    R-stats 
BuildRequires:    R-MASS 
Requires:         R-CRAN-glmnet >= 2.0.18
Requires:         R-CRAN-Rdpack >= 0.11.0
Requires:         R-CRAN-knockoff 
Requires:         R-CRAN-spcov 
Requires:         R-CRAN-xgboost 
Requires:         R-stats 
Requires:         R-MASS 

%description
A novel strategy for conducting variable selection without prior model
topology knowledge using the knockoff method (Barber and Candes (2015)
<doi:10.1214/15-AOS1337>) with extreme boosted tree models (Chen and
Guestrin (2016) <doi:10.1145/2939672.2939785>). This method is inspired by
the original knockoff method, where the differences between original and
knockoff variables are used for variable selection with false discovery
rate control. In addition to the original knockoff generating methods, two
new sampling methods are available to be implemented, namely the sparse
covariance and principal component knockoff methods. As results, the
indices of selected variables are returned.

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
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/REFERENCES.bib
%{rlibdir}/%{packname}/INDEX
