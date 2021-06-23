%global __brp_check_rpaths %{nil}
%global packname  tfaddons
%global packver   0.10.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.10.0
Release:          3%{?dist}%{?buildtag}
Summary:          Interface to 'TensorFlow SIG Addons'

License:          Apache License 2.0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-reticulate 
BuildRequires:    R-CRAN-tensorflow 
BuildRequires:    R-CRAN-rstudioapi 
BuildRequires:    R-CRAN-keras 
BuildRequires:    R-CRAN-purrr 
Requires:         R-CRAN-reticulate 
Requires:         R-CRAN-tensorflow 
Requires:         R-CRAN-rstudioapi 
Requires:         R-CRAN-keras 
Requires:         R-CRAN-purrr 

%description
'TensorFlow SIG Addons' <https://www.tensorflow.org/addons> is a
repository of community contributions that conform to well-established API
patterns, but implement new functionality not available in core
'TensorFlow'. 'TensorFlow' natively supports a large number of operators,
layers, metrics, losses, optimizers, and more. However, in a fast moving
field like Machine Learning, there are many interesting new developments
that cannot be integrated into core 'TensorFlow' (because their broad
applicability is not yet clear, or it is mostly used by a smaller subset
of the community).

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
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
