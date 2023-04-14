%global __brp_check_rpaths %{nil}
%global packname  helixvis
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          3%{?dist}%{?buildtag}
Summary:          Visualize Alpha-Helical Peptide Sequences

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.0.0
BuildRequires:    R-CRAN-rlang >= 0.2.2
BuildRequires:    R-CRAN-ggforce >= 0.1.3
Requires:         R-CRAN-ggplot2 >= 3.0.0
Requires:         R-CRAN-rlang >= 0.2.2
Requires:         R-CRAN-ggforce >= 0.1.3

%description
Create publication-quality, 2-dimensional visualizations of alpha-helical
peptide sequences. Specifically, allows the user to programmatically
generate helical wheels and wenxiang diagrams to provide a bird's eye,
top-down view of alpha-helical oligopeptides. See Wadhwa RR, et al. (2018)
<doi:10.21105/joss.01008> for more information.

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
