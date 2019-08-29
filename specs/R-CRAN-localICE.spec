%global packname  localICE
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}
Summary:          Local Individual Conditional Expectation

License:          BSD_3_clause + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-checkmate 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-checkmate 

%description
Local Individual Conditional Expectation is as an extension to Individual
Conditional Expectation (ICE) and provides three-dimensional local
explanations for particular data instances. The three dimension are two
features at the horizontal and vertical axes as well as the target that is
represented by different colors. The approach is applicable for
classification and regression problems to explain interactions of two
features towards the target. The plot for discrete targets looks similar
to plots of cluster algorithms like k-means, where different clusters
represent different predictions. Reference to the ICE approach: Alex
Goldstein, Adam Kapelner, Justin Bleich, Emil Pitkin (2013)
<arXiv:1309.6392>.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
