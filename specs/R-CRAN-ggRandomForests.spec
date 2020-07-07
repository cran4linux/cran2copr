%global packname  ggRandomForests
%global packver   2.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.1
Release:          3%{?dist}
Summary:          Visually Exploring Random Forests

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-randomForestSRC >= 1.5.5
BuildRequires:    R-CRAN-randomForest 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-survival 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-tidyr 
Requires:         R-CRAN-randomForestSRC >= 1.5.5
Requires:         R-CRAN-randomForest 
Requires:         R-CRAN-ggplot2 
Requires:         R-survival 
Requires:         R-parallel 
Requires:         R-CRAN-tidyr 

%description
Graphic elements for exploring Random Forests using the 'randomForest' or
'randomForestSRC' package for survival, regression and classification
forests and 'ggplot2' package plotting.

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
