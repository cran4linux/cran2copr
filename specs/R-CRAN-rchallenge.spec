%global packname  rchallenge
%global packver   1.3.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.2
Release:          3%{?dist}
Summary:          A Simple Data Science Challenge System

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


Requires:         pandoc
BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-knitr >= 1.6
BuildRequires:    R-CRAN-rmarkdown >= 0.5
Requires:         R-CRAN-knitr >= 1.6
Requires:         R-CRAN-rmarkdown >= 0.5

%description
A simple data science challenge system using R Markdown and 'Dropbox'
<https://www.dropbox.com/>. It requires no network configuration, does not
depend on external platforms like e.g. 'Kaggle' <https://www.kaggle.com/>
and can be easily installed on a personal computer.

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
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/template
%{rlibdir}/%{packname}/INDEX
