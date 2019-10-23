%global packname  orgR
%global packver   0.9.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.9.0
Release:          1%{?dist}
Summary:          Analyse Text Files Created by Emacs' Org mode

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-data.table >= 1.9.4
BuildRequires:    R-CRAN-ggthemes >= 1.7.0
BuildRequires:    R-CRAN-lubridate >= 1.3.3
BuildRequires:    R-CRAN-ggplot2 >= 1.0.0
BuildRequires:    R-CRAN-stringr >= 0.6.2
Requires:         R-CRAN-data.table >= 1.9.4
Requires:         R-CRAN-ggthemes >= 1.7.0
Requires:         R-CRAN-lubridate >= 1.3.3
Requires:         R-CRAN-ggplot2 >= 1.0.0
Requires:         R-CRAN-stringr >= 0.6.2

%description
Provides functionality to process text files created by Emacs' Org mode,
and decompose the content to the smallest components (headlines, body,
tag, clock entries etc).  Emacs is an extensible, customizable text editor
and Org mode is for keeping notes, maintaining TODO lists, planning
projects.  Allows users to analyze org files as data frames in R, e.g., to
convieniently group tasks by tag into project and calculate total working
hours.  Also provides some help functions like search.parent, gg.pie
(visualise working hours in ggplot2) and tree.headlines (visualise
headline stricture in tree format) to help user managing their complex org
files.

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
