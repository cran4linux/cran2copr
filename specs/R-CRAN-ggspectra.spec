%global packname  ggspectra
%global packver   0.3.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.4
Release:          1%{?dist}
Summary:          Extensions to 'ggplot2' for Radiation Spectra

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.1.1
BuildRequires:    R-CRAN-lubridate >= 1.7.4
BuildRequires:    R-CRAN-scales >= 1.0.0
BuildRequires:    R-CRAN-photobiology >= 0.9.29
BuildRequires:    R-CRAN-tidyr >= 0.8.3
BuildRequires:    R-CRAN-ggrepel >= 0.8.1
BuildRequires:    R-CRAN-dplyr >= 0.8.1
BuildRequires:    R-CRAN-photobiologyWavebands >= 0.4.3
Requires:         R-CRAN-ggplot2 >= 3.1.1
Requires:         R-CRAN-lubridate >= 1.7.4
Requires:         R-CRAN-scales >= 1.0.0
Requires:         R-CRAN-photobiology >= 0.9.29
Requires:         R-CRAN-tidyr >= 0.8.3
Requires:         R-CRAN-ggrepel >= 0.8.1
Requires:         R-CRAN-dplyr >= 0.8.1
Requires:         R-CRAN-photobiologyWavebands >= 0.4.3

%description
Additional annotations, stats, geoms and scales for plotting "light"
spectra with 'ggplot2', together with specializations of ggplot() and
autoplot() methods for spectral data and waveband definitions stored in
objects of classes defined in package 'photobiology'. Part of the
'r4photobiology' suite, Aphalo P. J. (2015)
<doi:10.19232/uv4pb.2015.1.14>.

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
