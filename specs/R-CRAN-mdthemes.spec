%global __brp_check_rpaths %{nil}
%global packname  mdthemes
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          2%{?dist}%{?buildtag}
Summary:          Markdown Themes for 'ggplot2'

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.3.0
BuildRequires:    R-CRAN-cowplot 
BuildRequires:    R-CRAN-hrbrthemes 
BuildRequires:    R-CRAN-ggtext 
BuildRequires:    R-CRAN-ggthemes 
BuildRequires:    R-CRAN-tvthemes 
Requires:         R-CRAN-ggplot2 >= 3.3.0
Requires:         R-CRAN-cowplot 
Requires:         R-CRAN-hrbrthemes 
Requires:         R-CRAN-ggtext 
Requires:         R-CRAN-ggthemes 
Requires:         R-CRAN-tvthemes 

%description
A collection of 'ggplot2' themes that render text as markdown/HTML. This
enables the creation of complex formatted plot labels, e.g. titles with
individual words highlighted in different colors.

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
%{rlibdir}/%{packname}/DESCRIPTION
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
