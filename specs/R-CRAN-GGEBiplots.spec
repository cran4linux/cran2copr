%global __brp_check_rpaths %{nil}
%global packname  GGEBiplots
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          3%{?dist}%{?buildtag}
Summary:          GGE Biplots with 'ggplot2'

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.1
Requires:         R-core >= 3.3.1
BuildArch:        noarch
BuildRequires:    R-grDevices >= 3.3.1
BuildRequires:    R-stats >= 3.3.1
BuildRequires:    R-grid >= 3.3.1
BuildRequires:    R-utils >= 3.3.1
BuildRequires:    R-CRAN-ggplot2 >= 2.2.0
BuildRequires:    R-CRAN-gge >= 1.2
BuildRequires:    R-CRAN-GGEBiplotGUI >= 1.0.9
BuildRequires:    R-CRAN-scales >= 0.4.1
BuildRequires:    R-CRAN-ggforce >= 0.1.1
Requires:         R-grDevices >= 3.3.1
Requires:         R-stats >= 3.3.1
Requires:         R-grid >= 3.3.1
Requires:         R-utils >= 3.3.1
Requires:         R-CRAN-ggplot2 >= 2.2.0
Requires:         R-CRAN-gge >= 1.2
Requires:         R-CRAN-GGEBiplotGUI >= 1.0.9
Requires:         R-CRAN-scales >= 0.4.1
Requires:         R-CRAN-ggforce >= 0.1.1

%description
Genotype plus genotype-by-environment (GGE) biplots rendered using
'ggplot2'. Provides a command line interface to all of the functionality
contained within 'GGEBiplotGUI'.

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
