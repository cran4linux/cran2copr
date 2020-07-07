%global packname  formulaic
%global packver   0.0.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.7
Release:          3%{?dist}
Summary:          Dynamic Generation and Quality Checks of Formula Objects

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-data.table 
Requires:         R-CRAN-data.table 

%description
Many statistical models and analyses in R are implemented through formula
objects. The formulaic package creates a unified approach for
programmatically and dynamically generating formula objects. Users may
specify the outcome and inputs of a model directly, search for variables
to include based upon naming patterns, incorporate interactions, and
identify variables to exclude. A wide range of quality checks are
implemented to identify issues such as misspecified variables,
duplication, a lack of contrast in the inputs, and a large number of
levels in categorical data.  Variables that do not meet these quality
checks can be automatically excluded from the model.  These issues are
documented and reported in a manner that provides greater accountability
and useful information to guide an investigation of the data.

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
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
