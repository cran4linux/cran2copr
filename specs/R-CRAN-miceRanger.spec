%global packname  miceRanger
%global packver   1.3.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.1
Release:          1%{?dist}
Summary:          Multiple Imputation by Chained Equations with Random Forests

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ranger 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-FNN 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-crayon 
BuildRequires:    R-CRAN-corrplot 
BuildRequires:    R-CRAN-ggpubr 
BuildRequires:    R-CRAN-DescTools 
BuildRequires:    R-CRAN-foreach 
Requires:         R-CRAN-ranger 
Requires:         R-CRAN-data.table 
Requires:         R-stats 
Requires:         R-CRAN-FNN 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-crayon 
Requires:         R-CRAN-corrplot 
Requires:         R-CRAN-ggpubr 
Requires:         R-CRAN-DescTools 
Requires:         R-CRAN-foreach 

%description
Multiple Imputation has been shown to be a flexible method to impute
missing values by Van Buuren (2007) <doi:10.1177/0962280206074463>.
Expanding on this, random forests have been shown to be an accurate model
by Stekhoven and Buhlmann <arXiv:1105.0828> to impute missing values in
datasets. They have the added benefits of returning out of bag error and
variable importance estimates, as well as being simple to run in parallel.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
