%global packname  qmethod
%global packver   1.5.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.5.4
Release:          1%{?dist}
Summary:          Analysis of Subjective Perspectives Using Q Methodology

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-psych 
BuildRequires:    R-CRAN-GPArotation 
BuildRequires:    R-tools 
BuildRequires:    R-CRAN-digest 
BuildRequires:    R-CRAN-knitr 
BuildRequires:    R-CRAN-xtable 
Requires:         R-methods 
Requires:         R-CRAN-psych 
Requires:         R-CRAN-GPArotation 
Requires:         R-tools 
Requires:         R-CRAN-digest 
Requires:         R-CRAN-knitr 
Requires:         R-CRAN-xtable 

%description
Analysis of Q methodology, used to identify distinct perspectives existing
within a group. This methodology is used across social, health and
environmental sciences to understand diversity of attitudes, discourses,
or decision-making styles (for more information, see
<http://qmethod.org>). A single function runs the full analysis. Each step
can be run separately using the corresponding functions: for automatic
flagging of Q-sorts (manual flagging is optional), for statement scores,
for distinguishing and consensus statements, and for general
characteristics of the factors. Additional functions are available to
import and export data, to print and plot, to import raw data from
individual *.CSV files, and to make printable cards. The package also
offers functions to print Q cards and to generate Q distributions for
study administration. The package uses principal components and it allows
manual or automatic flagging, a number of mathematical methods for
rotation, and a number of correlation coefficients for the initial
correlation matrix. See further details in the package documentation, and
in the web pages below, which include a cookbook, guidelines for more
advanced analysis (how to perform manual flagging or change the sign of
factors), data management, and a beta graphical user interface for online
and offline use.

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
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/cardtemplates
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/INDEX
