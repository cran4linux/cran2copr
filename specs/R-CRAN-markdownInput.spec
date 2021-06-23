%global __brp_check_rpaths %{nil}
%global packname  markdownInput
%global packver   0.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.2
Release:          3%{?dist}%{?buildtag}
Summary:          Shiny Module for a Markdown Input with Result Preview

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-shiny >= 1.0.5
BuildRequires:    R-CRAN-shinyAce 
BuildRequires:    R-CRAN-markdown 
Requires:         R-CRAN-shiny >= 1.0.5
Requires:         R-CRAN-shinyAce 
Requires:         R-CRAN-markdown 

%description
An R-Shiny module containing a "markdownInput". This input allows the user
to write some markdown code and to preview the result. This input has been
inspired by the "comment" window of <https://github.com/>.

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
%doc %{rlibdir}/%{packname}/ShinyExample
%{rlibdir}/%{packname}/INDEX
