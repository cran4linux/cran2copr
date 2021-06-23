%global __brp_check_rpaths %{nil}
%global packname  caretEnsemble
%global packver   2.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.1
Release:          3%{?dist}%{?buildtag}
Summary:          Ensembles of Caret Models

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildArch:        noarch
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-pbapply 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-digest 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-lattice 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-caret 
Requires:         R-methods 
Requires:         R-CRAN-pbapply 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-digest 
Requires:         R-CRAN-plyr 
Requires:         R-lattice 
Requires:         R-CRAN-gridExtra 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-caret 

%description
Functions for creating ensembles of caret models: caretList() and
caretStack().  caretList() is a convenience function for fitting multiple
caret::train() models to the same dataset. caretStack() will make linear
or non-linear combinations of these models, using a caret::train() model
as a meta-model, and caretEnsemble() will make a robust linear combination
of models using a GLM.

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
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/data-raw
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
