%global packname  integr
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          2%{?dist}
Summary:          An Implementation of Interaction Graphs of Aleks Jakulin

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-gtools >= 3.5.0
BuildRequires:    R-utils >= 3.5.0
BuildRequires:    R-CRAN-rsvg >= 1.3
BuildRequires:    R-CRAN-DiagrammeR >= 1.0.0
BuildRequires:    R-CRAN-dplyr >= 0.7.6
BuildRequires:    R-CRAN-DiagrammeRsvg >= 0.1
Requires:         R-CRAN-gtools >= 3.5.0
Requires:         R-utils >= 3.5.0
Requires:         R-CRAN-rsvg >= 1.3
Requires:         R-CRAN-DiagrammeR >= 1.0.0
Requires:         R-CRAN-dplyr >= 0.7.6
Requires:         R-CRAN-DiagrammeRsvg >= 0.1

%description
Generates a 'Graphviz' graph of the most significant 3-way interaction
gains (i.e. conditional information gains) based on a provided discrete
data frame. Various output formats are supported ('Graphviz', SVG, PNG,
PDF, PS). For references, see the webpage of Aleks Jakulin
<http://stat.columbia.edu/~jakulin/Int/>.

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
