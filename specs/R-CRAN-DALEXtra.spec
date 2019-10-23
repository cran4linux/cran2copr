%global packname  DALEXtra
%global packver   0.1.8
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.8
Release:          1%{?dist}
Summary:          Extension for 'DALEX' Package

License:          GPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-DALEX >= 0.4.7
BuildRequires:    R-CRAN-reticulate 
BuildRequires:    R-CRAN-ggplot2 
Requires:         R-CRAN-DALEX >= 0.4.7
Requires:         R-CRAN-reticulate 
Requires:         R-CRAN-ggplot2 

%description
Provides wrapper of various machine learning models. In applied machine
learning, there is a strong belief that we need to strike a balance
between interpretability and accuracy. However, in field of the
interpretable machine learning, there are more and more new ideas for
explaining black-box models, that are implemented in 'R'. 'DALEXtra'
creates 'DALEX' Biecek (2018) <arXiv:1806.08915> explainer for many type
of models including those created using 'python' 'scikit-learn' and
'keras' libraries.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/ChampionChallenger
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/INDEX
