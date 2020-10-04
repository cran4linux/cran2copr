%global packname  leafSTAR
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          3%{?dist}%{?buildtag}
Summary:          Silhouette to Area Ratio of Tilted Surfaces

License:          AGPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.1
Requires:         R-core >= 3.4.1
BuildArch:        noarch

%description
Implementation of trigonometric functions to calculate the exposure of
flat, tilted surfaces, such as leaves and slopes, to direct solar
radiation. It implements the equations in A.G. Escribano-Rocafort, A.
Ventre-Lespiaucq, C. Granado-Yela, et al. (2014)
<doi:10.1111/2041-210X.12141> in a few user-friendly R functions. All
functions handle data obtained with 'Ahmes' 1.0 for Android, as well as
more traditional data sources (compass, protractor, inclinometer). The
main function (star()) calculates the potential exposure of flat, tilted
surfaces to direct solar radiation (silhouette to area ratio, STAR). It is
equivalent to the ratio of the leaf projected area to total leaf area, but
instead of using area data it uses spatial position angles, such as pitch,
roll and course, and information on the geographical coordinates, hour,
and date. The package includes additional functions to recalculate STAR
with custom settings of location and time, to calculate the tilt angle of
a surface, and the minimum angle between two non-orthogonal planes.

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
%{rlibdir}/%{packname}/INDEX
