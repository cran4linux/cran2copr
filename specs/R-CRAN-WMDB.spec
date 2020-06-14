%global packname  WMDB
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          2%{?dist}
Summary:          Discriminant Analysis Methods by Weight Mahalanobis Distance andbayes

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch

%description
Distance discriminant analysis method is one of classification methods
according to multiindex performance parameters.However,the traditional
Mahalanobis distance discriminant method treats with the importance of all
parameters equally,and exaggerates the role of parameters which changes a
little.The weighted Mahalanobis distance is used in discriminant analysis
method to distinguish the importance of each parameter.In the concrete
application,firstly based on the principal component analysis scheme,a new
group of parameters and their corresponding percent contributions of the
parameters are calculated ,and the weighted matrix is regarded as the
diagonal matrix of the contributions rates.Setting data to
standardization,then the weighted Mahalanobis distance can be
calculated.Besides the methods metioned above,bayes method is also given.

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
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
