%global packname  pysd2r
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          3%{?dist}
Summary:          API to 'Python' Library 'pysd'

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3
Requires:         R-core >= 3.3
BuildArch:        noarch
BuildRequires:    R-CRAN-knitr 
BuildRequires:    R-CRAN-reticulate 
BuildRequires:    R-CRAN-tibble 
Requires:         R-CRAN-knitr 
Requires:         R-CRAN-reticulate 
Requires:         R-CRAN-tibble 

%description
Using the R package 'reticulate', this package creates an interface to the
'pysd' toolset. The package provides an R interface to a number of 'pysd'
functions, and can read files in 'Vensim' 'mdl' format, and 'xmile'
format. The resulting simulations are returned as a 'tibble', and from
that the results can be processed using 'dplyr' and 'ggplot2'. The package
has been tested using 'python3'.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/models
%{rlibdir}/%{packname}/INDEX
