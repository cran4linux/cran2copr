%global __brp_check_rpaths %{nil}
%global packname  murphydiagram
%global packver   0.12.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.12.2
Release:          3%{?dist}%{?buildtag}
Summary:          Murphy Diagrams for Forecast Comparisons

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch

%description
Data and code for the paper by Ehm, Gneiting, Jordan and Krueger ('Of
Quantiles and Expectiles: Consistent Scoring Functions, Choquet
Representations, and Forecast Rankings', JRSS-B, 2016
<DOI:10.1111/rssb.12154>).

%prep
%setup -q -c -n %{packname}


%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}

test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%{rlibdir}/%{packname}
