%global __brp_check_rpaths %{nil}
%global packname  chromoMap
%global packver   0.3.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.1
Release:          1%{?dist}%{?buildtag}
Summary:          Interactive Genomic Visualization of Biological Data

License:          GPL-3 | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0
Requires:         R-core >= 4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-htmlwidgets >= 1.0
BuildRequires:    R-CRAN-htmltools >= 0.3.6
Requires:         R-CRAN-htmlwidgets >= 1.0
Requires:         R-CRAN-htmltools >= 0.3.6

%description
Provides interactive, configurable and elegant graphics visualization of
the chromosomes or chromosome regions of any living organism allowing
users to map chromosome elements (like genes, SNPs etc.) on the chromosome
plot. It introduces a special plot viz. the "chromosome heatmap" that, in
addition to mapping elements, can visualize the data associated with
chromosome elements (like gene expression) in the form of heat colors
which can be highly advantageous in the scientific interpretations and
research work. Because of the large size of the chromosomes, it is
impractical to visualize each element on the same plot. However, the plot
provides a magnified view for each of chromosome locus to render
additional information and visualization specific for that location. You
can map thousands of genes and can view all mappings easily. Users can
investigate the detailed information about the mappings (like gene names
or total genes mapped on a location) or can view the magnified single or
double stranded view of the chromosome at a location showing each mapped
element in sequential order. The package provide multiple features like
visualizing multiple sets, chromosome heat-maps, group annotations, adding
hyperlinks, and labelling. The plots can be saved as HTML documents that
can be customized and shared easily. In addition, you can include them in
R Markdown or in R 'Shiny' applications.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
# don't allow local prefix in executable scripts
find -type f -executable -exec sed -Ei 's@#!( )*/usr/local/bin@#!/usr/bin@g' {} \;

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
# remove buildroot from installed files
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
