%global packname  wooldridge
%global packver   1.3.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.1
Release:          2%{?dist}
Summary:          111 Data Sets from "Introductory Econometrics: A ModernApproach, 6e" by Jeffrey M. Wooldridge

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildArch:        noarch

%description
Students learning both econometrics and R may find the introduction to
both challenging. However, if the text is "Introductory Econometrics: A
Modern Approach" by Jeffrey M. Wooldridge, they are in luck! The
wooldridge data package aims to lighten the task by efficiently loading
any data set found in the text with a single command. Data sets have all
been compressed to a fraction of their original size and are well
documented. Documentation files contain the page numbers of the text where
each set is used, the original source, time of publication, and notes
suggesting ideas for further exploratory data analysis and research. If
one need's to brush-up on model syntax, a vignette contains R solutions to
examples from each chapter of the text. Data sets are from the 6th edition
(Wooldridge 2016, ISBN-13: 978-1-305-27010-7), and are backwards
compatible with all versions of the text.

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
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
