%global packname  VICmodel
%global packver   0.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.2
Release:          1%{?dist}
Summary:          The Variable Infiltration Capacity (VIC) Model

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildRequires:    R-CRAN-Rcpp >= 0.12.0
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-foreach 
Requires:         R-CRAN-Rcpp >= 0.12.0
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-foreach 

%description
The Variable Infiltration Capacity (VIC) model is a macroscale hydrologic
model that solves full water and energy balances, originally developed by
Xu Liang at the University of Washington (UW). The version of VIC source
code used is of 5.0.1 on <https://github.com/UW-Hydro/VIC/>, see Hamman et
al. (2018). Development and maintenance of the current official version of
the VIC model at present is led by the UW Hydro (Computational Hydrology
group) in the Department of Civil and Environmental Engineering at UW. VIC
is a research model and in its various forms it has been applied to most
of the major river basins around the world, as well as globally. If you
make use of this model, please acknowledge the appropriate references
listed in the help page of this package or on the references page
<http://vic.readthedocs.io/en/master/Documentation/References/> of the VIC
official documentation website. These should include Liang et al. (1994)
plus any references relevant to the features you are using Reference:
Liang, X., D. P. Lettenmaier, E. F. Wood, and S. J. Burges (1994), A
simple hydrologically based model of land surface water and energy fluxes
for general circulation models, J. Geophys. Res., 99(D7), 14415-14428,
<doi:10.1029/94JD00483>. Hamman et al. (2018) about VIC 5.0.1 also can be
considered: Hamman, J. J., Nijssen, B., Bohn, T. J., Gergel, D. R., and
Mao, Y. (2018), The Variable Infiltration Capacity model version 5
(VIC-5): infrastructure improvements for new applications and
reproducibility, Geosci. Model Dev., 11, 3481-3496,
<doi:10.5194/gmd-11-3481-2018>.

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
%doc %{rlibdir}/%{packname}/COPYRIGHTS
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
