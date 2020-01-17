%global packname  tfhub
%global packver   0.7.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.7.0
Release:          1%{?dist}
Summary:          Interface to 'TensorFlow' Hub

License:          Apache License 2.0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-reticulate >= 1.9.9002
BuildRequires:    R-CRAN-tensorflow >= 1.8.0.9006
BuildRequires:    R-CRAN-rstudioapi >= 0.7
BuildRequires:    R-CRAN-magrittr 
Requires:         R-CRAN-reticulate >= 1.9.9002
Requires:         R-CRAN-tensorflow >= 1.8.0.9006
Requires:         R-CRAN-rstudioapi >= 0.7
Requires:         R-CRAN-magrittr 

%description
'TensorFlow' Hub is a library for the publication, discovery, and
consumption of reusable parts of machine learning models. A module is a
self-contained piece of a 'TensorFlow' graph, along with its weights and
assets, that can be reused across different tasks in a process known as
transfer learning. Transfer learning train a model with a smaller dataset,
improve generalization, and speed up training.

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
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
